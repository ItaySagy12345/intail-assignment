import QuotesList from "@/components/QuotesList/QuotesList";
import styles from './QuotesPage.module.scss';
import useQuotesPage from "./useQuotesPage";

function QuotesPage() {
    const {
        quotes
    } = useQuotesPage();

    return (
        <div className={styles.quotesPage}>
            <QuotesList quotes={quotes} />
        </div>
    );
}

export default QuotesPage;