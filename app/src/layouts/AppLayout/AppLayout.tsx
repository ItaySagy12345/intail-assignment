import styles from './AppLayout.module.scss';
import Sidebar from '../components/Sidebar/Sidebar';
import { Outlet } from 'react-router-dom';

function AppLayout() {
    return (
        <div className={styles.appLayout}>
            <Sidebar />
            <div className={styles.page}>
                <Outlet />
            </div>
        </div>
    );
}

export default AppLayout;