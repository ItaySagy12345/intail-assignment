import * as QuotesService from 'services/quotes-service';
import styles from './QuotesPage.module.scss';
import { useEffect, useState } from "react";
import { APIFilter } from "generics/interfaces/api-interfaces";
import { Quote } from "generics/interfaces/models/quote";
import QuotesList from "components/QuotesList/QuotesList";

function QuotesPage() {
  const PAGE = 1;
  const SIZE = 10;

  const [filter, setFilter] = useState<APIFilter>({ page: PAGE, size: SIZE });
  const [quotes, setQuotes] = useState<Quote[]>([]);

  useEffect(() => {
    fetchQuotes();
  }, [filter]);

  const fetchQuotes = async (): Promise<void> => {
    const { data: quotes } = await QuotesService.listQuotes(filter);
    setQuotes((prevState: Quote[]): Quote[] => [...prevState, ...quotes]);
  };

  useEffect(() => {
    console.log(quotes);
  }, [quotes]);

  useEffect(() => {
    console.log(filter);
  }, [filter]);

  const handleFetchQuotes = () => {
    const incrementedFilter: APIFilter = { ...filter, page: filter.page + 1 };
    setFilter(incrementedFilter);
  };

  return (
    <div className={styles.quotesPage}>
      <h1 className={styles.header}>Knowledge is power, hide it well!</h1>
      <QuotesList quotes={quotes} onfetchQuotes={handleFetchQuotes} />
    </div>
  );
}

export default QuotesPage;