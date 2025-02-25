import * as QuotesService from 'services/quotes-service';

import QuotesList from "components/QuotesList/QuotesList";
import Logo from "components/Logo/Logo";
import styles from './QuotesPage.module.scss';

import { useEffect, useState } from "react";
import { APIFilter } from "generics/interfaces/api-interfaces";
import { Quote } from "generics/interfaces/models/quote";

const PAGE = 1;
const SIZE = 10;
const MAX_PAGE = 5;

function QuotesPage() {
  const [filter, setFilter] = useState<APIFilter>({ page: PAGE, size: SIZE });
  const [quotes, setQuotes] = useState<Quote[]>([]);

  useEffect(() => {
    fetchQuotes();
  }, [filter]);

  const handleFetchQuotes = (): void => {
    if (filter.page === MAX_PAGE) return;
    setFilter((prevState: APIFilter): APIFilter => ({ ...prevState, page: prevState.page + 1 }));
  };

  const fetchQuotes = async (): Promise<void> => {
    const { data: quotes } = await QuotesService.listQuotes(filter);
    setQuotes((prevState: Quote[]): Quote[] => [...prevState, ...quotes]);
  };

  return (
    <div className={styles.quotesPage}>
      <div className={styles.headerWrapper}>
        <Logo className={styles.logo} />
        <h1 className={styles.header}>Knowledge is power, hide it well!</h1>
      </div>

      <QuotesList quotes={quotes} onScrollEnd={handleFetchQuotes} />
    </div>
  );
}

export default QuotesPage;