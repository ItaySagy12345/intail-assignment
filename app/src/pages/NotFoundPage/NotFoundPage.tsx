import Button from "components/Button/Button";

import { useNavigate } from 'react-router-dom';
import { Routes } from "generics/enums/routes-enums";

import styles from './NotFoundPage.module.scss';

function NotFoundPage() {
  const navigate = useNavigate();

  const handleBackHomeClick = (): void => {
    navigate(Routes.HOME);
  };

  return (
    <div className={styles.notFoundPage}>
      <h1>404 Not Found</h1>
      <Button secondary onClick={handleBackHomeClick}>
        Back Home
      </Button>
    </div>
  );
}

export default NotFoundPage;