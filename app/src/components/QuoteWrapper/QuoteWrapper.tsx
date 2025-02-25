import * as AuthorsService from 'services/authors-service';
import styles from './QuoteWrapper.module.scss';
import { useState } from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faChevronDown, faChevronUp } from '@fortawesome/free-solid-svg-icons';
import QuoteStat from '../QuoteStat/QuoteStat';
import { Quote } from "generics/interfaces/models/quote";
import { Author } from "generics/interfaces/models/author";
import Button from "components/Button/Button";
import { Book } from "generics/interfaces/models/book";
import Error from "components/Error/Error";

interface QuoteProps {
  quote: Quote;
}

function QuoteWrapper({ quote }: QuoteProps) {
  const [dropdown, setDropdown] = useState<boolean>(false);
  const [author, setAuthor] = useState<Author | null>(null);
  const [isLoading, setIsLoading] = useState<boolean>(false);
  const [error, setError] = useState<string | null>(null);

  const handleEnhanceClick = async (authorName: string): Promise<void> => {
    if (!author) {
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

    setDropdown(!dropdown);
  };

  const handleToggleDropdown = (): void => {
    setDropdown(!dropdown);
  };

  const fetchAuthor = async (authorName: string): Promise<void> => {
    const { data: author } = await AuthorsService.getAuthor(authorName);
    setAuthor(author);
  };

  return (
    <div className={styles.quoteWrapper}>
      <div className={styles.staticInfo}>
        <Button loading={isLoading} disabled={isLoading} onClick={() => handleEnhanceClick(quote.author)}>Enhance</Button>
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

      <FontAwesomeIcon className={styles.toggleDropdown} icon={dropdown ? faChevronUp : faChevronDown} onClick={handleToggleDropdown} />
    </div>
  );
}

export default QuoteWrapper;