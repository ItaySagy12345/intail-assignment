import { Link } from 'react-router-dom';
import styles from './NotFoundPage.module.scss';

function NotFoundPage() {
  return (
    <div className={styles.notFoundPage}>
      <h1> You Wandered Off...<Link to='/'>Take me back</Link></h1>
    </div>
  );
}

export default NotFoundPage;