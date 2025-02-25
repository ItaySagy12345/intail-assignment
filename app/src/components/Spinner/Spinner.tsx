import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faSpinner } from "@fortawesome/free-solid-svg-icons";

function Spinner() {
  return (
    <FontAwesomeIcon icon={faSpinner} spin />
  );
}

export default Spinner;