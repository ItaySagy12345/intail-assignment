import HomePage from "@/pages/HomePage/HomePage";
import QuotesPage from "@/pages/QuotesPage/QuotesPage";

const appRouter = [
  {
    path: '',
    children: [
      {
        index: true,
        element: <HomePage />
      },
      {
        path: 'quotes',
        children: [
          {
            index: true,
            element: <QuotesPage />
          }
        ]
      }
    ]
  }
];

export default appRouter;