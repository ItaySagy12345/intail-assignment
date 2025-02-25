import * as Config from 'config/config';

import AppLayout from "layouts/AppLayout/AppLayout";
import NotFoundPage from "pages/NotFoundPage/NotFoundPage";
import appRouter from "routes/appRouter";

import { createBrowserRouter } from "react-router-dom";

const defaultRouter = createBrowserRouter([
  {
    path: '',
    element: <AppLayout />,
    children: [...appRouter]
  },
  {
    path: '*',
    element: <NotFoundPage />
  }
], { basename: Config.ROUTER_BASENAME });

export default defaultRouter;
