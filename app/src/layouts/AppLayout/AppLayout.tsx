import { Outlet } from 'react-router-dom';

import styles from './AppLayout.module.scss';

function AppLayout() {
  return (
    <div className={styles.appLayout}>
      <Outlet />
    </div>
  );
}

export default AppLayout;