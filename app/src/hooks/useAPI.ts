import { Response } from "@/generics/interfaces/api-interfaces";
import { useEffect, useState } from "react";

interface useAPIReturn<T> {
  error: boolean;
  loading: boolean;
  response: Response<T>;
}

function useAPI<T>(fetcher: (...params: any) => Promise<Response<T>>, dependencies: any[] = []): useAPIReturn<T> {
  const [response, setResponse] = useState<Response<T>>({} as Response);
  const [loading, setLoading] = useState<boolean>(false);
  const [error, setError] = useState<boolean>(false);

  useEffect(() => {
    fetch();
  }, [...dependencies]);

  const fetch = async (): Promise<void> => {
    setLoading(true);

    try {
      const response: any = await fetcher();
      setLoading(false);
      setResponse(response.data);
    } catch (e: any) {
      setError(true);
    } finally {
      setLoading(false);
    }
  };

  return {
    error,
    loading,
    response
  };
};

export default useAPI;