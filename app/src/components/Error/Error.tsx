import { faExclamationCircle } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import styles from './Error.module.scss';

interface ErrorProps {
    message: string;
}

function Error({ message }: ErrorProps) {
    return (
        <div className={styles.error}>
            <p>{message}</p>
            <FontAwesomeIcon icon={faExclamationCircle} />
        </div>
    );
}

export default Error;