import { Response } from "@/generics/interfaces/api-interfaces";
import { useEffect, useState } from "react";

interface useAPIReturn<T> {
  error: boolean;
  loading: boolean;
  response: Response<T>;
  updateData: (data: T, meta: Record<string, null> | null) => void;
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
      setResponse(response);
    } catch (e: any) {
      setError(true);
    } finally {
      setLoading(false);
    }
  };

  const updateData = (data: T, meta: Record<string, null> | null = null): void => {
    if (!meta) {
      meta = response.meta;
    }
    const updatedResponse: Response = { data, meta };
    setResponse(updatedResponse);
  };

  return {
    error,
    loading,
    response,
    updateData
  };
};

export default useAPI;