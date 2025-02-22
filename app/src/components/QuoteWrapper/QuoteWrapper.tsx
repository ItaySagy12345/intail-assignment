import { Quote } from '@/generics/interfaces/models/quote';
import styles from './QuoteWrapper.module.scss';

interface QuoteProps {
    quote: Quote;
}

function QuoteWrapper({ quote }: QuoteProps) {
    return (
        <div className={styles.quoteWrapper}>
            {quote.slug}
        </div>
    );
}

export default QuoteWrapper;