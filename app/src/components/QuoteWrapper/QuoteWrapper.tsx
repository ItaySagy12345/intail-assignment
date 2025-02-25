import * as AuthorsService from 'services/authors-service';

import Button from "components/Button/Button";
import Error from "components/Error/Error";
import QuoteStat from "components/QuoteStat/QuoteStat";

import { useState } from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faChevronDown, faChevronUp } from '@fortawesome/free-solid-svg-icons';
import { Quote } from "generics/interfaces/models/quote";
import { Author } from "generics/interfaces/models/author";
import { Book } from "generics/interfaces/models/book";

import styles from './QuoteWrapper.module.scss';

interface QuoteProps {
  quote: Quote;
}

function QuoteWrapper({ quote }: QuoteProps) {
  const [author, setAuthor] = useState<Author | null>(null);
  const [isLoading, setIsLoading] = useState<boolean>(false);
  const [error, setError] = useState<string | null>(null);
  const [dropdown, setDropdown] = useState<boolean>(false);

  const handleEnhanceClick = async (authorName: string): Promise<void> => {
    if (!author && !error) {
      try {
        setIsLoading(true);
        await fetchAuthor(authorName);
        setDropdown(true);
      } catch (_: any) {
        setError('Sorry, this author appears to be anonymous 👻');
        setDropdown(true);
      } finally {
        setIsLoading(false);
      }
    }

    toggleDropdown();
  };

  const handleToggleDropdownClick = (): void => {
    (author || error) && toggleDropdown();
  };

  const toggleDropdown = (): void => {
    setDropdown(!dropdown);
  };

  const fetchAuthor = async (authorName: string): Promise<void> => {
    const { data: author } = await AuthorsService.getAuthor(authorName);
    setAuthor(author);
  };

  return (
    <div className={styles.quoteWrapper}>
      <div className={styles.staticInfo}>
        <Button
          className={styles.enhanceButton}
          loading={isLoading}
          disabled={isLoading}
          onClick={() => handleEnhanceClick(quote.author)}>
          Enhance
        </Button>
        <div className={styles.info}>
          <p className={styles.text}>{quote.text}</p>
          <QuoteStat stat={'Author:'} value={quote.author} />
        </div>
      </div>

      {dropdown && author && (
        <div className={styles.dynamicInfo}>
          <QuoteStat stat={'Birth Date:'} value={author.birthDate} />
          <QuoteStat stat={'Death Date:'} value={author.deathDate} />
          <p className={styles.books}>
            {author.books.map((book: Book, index: number) => (
              <QuoteStat stat={`Book ${index + 1}:`} value={book.name} />
            ))}
          </p>
        </div>
      )}

      {dropdown && error && (
        <Error message={error} />
      )}

      <FontAwesomeIcon
        className={`${styles.toggleDropdown} ${(!author && !error) && styles.inactive}`}
        icon={dropdown ? faChevronUp : faChevronDown}
        onClick={handleToggleDropdownClick}
      />
    </div>
  );
}

export default QuoteWrapper;