import { Tab } from '@/generics/interfaces/tab-interfaces';
import styles from './Sidebar.module.scss';
import { Link } from 'react-router-dom';

function Sidebar() {
    const tabs: Tab[] = [{ id: 1, name: "Home", endpoint: '/' }, { id: 2, name: "Quotes", endpoint: '/quotes' }];

    return (
        <div className={styles.sidebar}>
            <div className={styles.tabs}>
                {tabs.map((tab: Tab) => (
                    <Link to={tab.endpoint} className={styles.tab} key={tab.id}>{tab.name}</Link>
                ))}
            </div>
        </div>
    );
}

export default Sidebar;