import styles from './Sidebar.module.scss';
import Logo from '@/components/Logo/Logo';
import Tabs from '@/components/Tabs/Tabs';

function Sidebar() {
    return (
        <div className={styles.sidebar}>
            <Logo />
            <Tabs />
        </div>
    );
}

export default Sidebar;