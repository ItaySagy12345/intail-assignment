import QuoteWrapper from "components/QuoteWrapper/QuoteWrapper";

import { useState, useEffect, useRef } from 'react';
import { Quote } from "generics/interfaces/models/quote";

import styles from './QuotesList.module.scss';

interface QuotesListProps {
  quotes: Quote[];
  onScrollEnd: () => void;
}

function QuotesList({ quotes, onScrollEnd }: QuotesListProps) {
  const [isFetching, setIsFetching] = useState<boolean>(false);

  const scrollContainerRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (!isFetching) return;
    setIsFetching(false);
  }, [quotes]);

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

  const handleScroll = (): void => {
    if (scrollContainerRef.current) {
      const { scrollTop, scrollHeight, clientHeight } = scrollContainerRef.current;

      if (scrollTop + clientHeight >= scrollHeight - 10 && !isFetching) {
        setIsFetching(true);
        onScrollEnd();
      }
    }
  };

  return (
    <div className={styles.quotesList} ref={scrollContainerRef}>
      {quotes.map((quote: Quote, index: number) => (
        <QuoteWrapper key={`${quote.slug}-${index}`} quote={quote} />
      ))}
    </div>
  );
}

export default QuotesList;