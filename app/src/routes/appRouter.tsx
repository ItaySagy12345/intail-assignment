import HomePage from "pages/HomePage/HomePage";
import QuotesPage from "pages/QuotesPage/QuotesPage";

import { Routes } from "generics/enums/routes-enums";

const appRouter = [
  {
    path: Routes.HOME,
    children: [
      {
        index: true,
        element: <HomePage />
      },
      {
        path: Routes.QUOTES,
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