import { useState, useEffect, useRef } from 'react';
import styles from './QuotesList.module.scss';
import { Quote } from "generics/interfaces/models/quote";
import QuoteWrapper from "components/QuoteWrapper/QuoteWrapper";

interface QuotesListProps {
  quotes: Quote[];
  onfetchQuotes: () => void;
}

function QuotesList({ quotes, onfetchQuotes }: QuotesListProps) {
  const [isFetching, setIsFetching] = useState(false);

  const scrollContainerRef = useRef<HTMLDivElement>(null);

  const handleScroll = () => {
    if (scrollContainerRef.current) {
      const { scrollTop, scrollHeight, clientHeight } = scrollContainerRef.current;
      if (scrollTop + clientHeight >= scrollHeight - 10 && !isFetching) {
        setIsFetching(true);
        onfetchQuotes();
      }
    }
  };

  useEffect(() => {
    const scrollContainer = scrollContainerRef.current;
    if (scrollContainer) {
      scrollContainer.addEventListener('scroll', handleScroll);
    }

    return () => {
      if (scrollContainer) {
        scrollContainer.removeEventListener('scroll', handleScroll);
      }
    };
  }, [isFetching]);

  useEffect(() => {
    if (!isFetching) return;
    setIsFetching(false);
  }, [quotes]);

  return (
    <div className={styles.quotesList} ref={scrollContainerRef}>
      {quotes.map((quote: Quote) => (
        <QuoteWrapper key={quote.slug} quote={quote} />
      ))}
      {isFetching && <div>Loading...</div>}
    </div>
  );
}

export default QuotesList;
