import { Quote } from '@/generics/interfaces/models/quote';
import styles from './QuotesList.module.scss';
import QuoteWrapper from '../QuoteWrapper/QuoteWrapper';

interface QuotesListProps {
    quotes: Quote[];
}

function QuotesList({ quotes }: QuotesListProps) {
    return (
        <div className={styles.quotesList}>
            {quotes.map((quote: Quote) => (
                <QuoteWrapper quote={quote} />
            ))}
        </div>
    );
}

export default QuotesList;