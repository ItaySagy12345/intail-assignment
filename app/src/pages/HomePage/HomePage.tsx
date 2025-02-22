import Button from '@/components/Button/Button';
import styles from './HomePage.module.scss';
import { useNavigate } from 'react-router-dom';
import { Routes } from '@/generics/enums/routes-enums';

function HomePage() {
    const navigate = useNavigate();

    const handleQuotesClick = (): void => {
        navigate(`/${Routes.QUOTES}`);
    };

    return (
        <div className={styles.homePage}>
            <h1>Welcome to Quote Master</h1>
            <Button secondary onClick={handleQuotesClick}>Give me wisdom</Button>
        </div>
    );
}

export default HomePage;