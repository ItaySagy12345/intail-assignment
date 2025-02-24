import QuotesList from "@/components/QuotesList/QuotesList";
import styles from './QuotesPage.module.scss';
import * as QuotesService from '@/services/quotes-service';
import useAPI from "@/hooks/useAPI";
import { APIFilter } from "@/generics/interfaces/api-interfaces";

function QuotesPage() {
    const filter: APIFilter = { page: 1, size: 10 };
    const { response: { data: quotes = [] } } = useAPI(() => QuotesService.listQuotes(filter));

    return (
        <div className={styles.quotesPage}>
            <h1 className={styles.header}>Knowledge is power, hide it well!</h1>
            <QuotesList quotes={quotes} />
        </div>
    );
}

export default QuotesPage;