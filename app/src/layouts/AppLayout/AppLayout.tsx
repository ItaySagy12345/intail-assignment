import styles from './AppLayout.module.scss';
import { Outlet } from 'react-router-dom';

function AppLayout() {
    return (
        <div className={styles.appLayout}>
            <Outlet />
        </div>
    );
}

export default AppLayout;