import * as QuotesService from '@/services/quotes-service';
import useAPI from "@/hooks/useAPI";

function useQuotesPage() {
  const { response: { data: quotes } } = useAPI(() => QuotesService.listQuotes());

  return {
    quotes
  };
}

export default useQuotesPage;