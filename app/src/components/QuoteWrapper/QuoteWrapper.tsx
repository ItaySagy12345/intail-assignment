import * as AuthorsService from '@/services/authors-service';
import { Quote } from '@/generics/interfaces/models/quote';
import styles from './QuoteWrapper.module.scss';
import Button from '../Button/Button';
import { useState } from 'react';
import { Author } from '@/generics/interfaces/models/author';
import Error from '../Error/Error';

interface QuoteProps {
    quote: Quote;
}

function QuoteWrapper({ quote }: QuoteProps) {
    const [isDropdownOpen, setIsDropdownOpen] = useState<boolean>(false);
    const [author, setAuthor] = useState<Author | null>(null);
    const [isLoading, setIsLoading] = useState<boolean>(false);
    const [error, setError] = useState<string | null>(null);

    const handleEnhanceClick = async (authorName: string): Promise<void> => {
        if (!author) {
            try {
                setIsLoading(true);
                await fetchAuthor(authorName);
                setIsDropdownOpen(true);
            } catch (e: any) {
                setError(e.message);
            } finally {
                setIsLoading(false);
            }
        }

        setIsDropdownOpen(!isDropdownOpen);
    };

    const fetchAuthor = async (authorName: string): Promise<void> => {
        const { data: author } = await AuthorsService.getAuthor(authorName);
        setAuthor(author);
    };

    return (
        <div className={styles.quoteWrapper}>
            <div className={styles.info}>
                <p className={styles.text}>{quote.text}</p>
                <p className={styles.author}>{quote.author}</p>
            </div>

            <Button loading={isLoading} onClick={() => handleEnhanceClick(quote.author)}>Enhance</Button>

            {author && (
                <div className={styles.authorInfo}>
                    <p>{author.name}</p>
                    <p>{author.birthDate}</p>
                    <p>{author.deathDate ?? 'N/A'}</p>
                </div>
            )}

            {error && (
                <Error message={error} />
            )}
        </div>
    );
}

export default QuoteWrapper;