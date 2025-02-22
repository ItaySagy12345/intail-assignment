import { Link } from 'react-router-dom';
import styles from './Tabs.module.scss';
import { Tab } from '@/generics/interfaces/tab-interfaces';
import { Routes } from '@/generics/enums/routes-enums';

function Tabs() {
    const tabs: Tab[] = [{ id: 1, name: "Home", endpoint: Routes.HOME }, { id: 2, name: "Quotes", endpoint: `/${Routes.QUOTES}` }];

    return (
        <div className={styles.tabs}>
            {tabs.map((tab: Tab) => (
                <Link className={styles.tab} to={tab.endpoint} key={tab.id}>{tab.name}</Link>
            ))}
        </div>
    );
}

export default Tabs;