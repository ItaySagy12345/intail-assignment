import * as Config from 'config/config';
import AppLayout from "layouts/AppLayout/AppLayout";
import { createBrowserRouter } from "react-router-dom";
import NotFoundPage from "pages/NotFoundPage/NotFoundPage";
import appRouter from "routes/appRouter";

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
