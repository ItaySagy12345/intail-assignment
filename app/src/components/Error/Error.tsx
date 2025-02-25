import { faExclamationCircle } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";

import styles from './Error.module.scss';

interface ErrorProps {
  message: string;
}

function Error({ message }: ErrorProps) {
  return (
    <div className={styles.error}>
      <FontAwesomeIcon className={styles.icon} icon={faExclamationCircle} />
      <p className={styles.message}>{message}</p>
    </div>
  );
}

export default Error;