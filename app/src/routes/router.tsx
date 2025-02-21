import * as Config from '@/config/config';
import appRouter from './appRouter';
import AppLayout from "@/layouts/AppLayout/AppLayout";
import NotFoundPage from '@/pages/NotFoundPage/NotFoundPage';
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
