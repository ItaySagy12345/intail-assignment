
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faSpinner } from '@fortawesome/free-solid-svg-icons';
import { MouseEvent } from "react";
import buttonClasses from './Button.module.scss';
import { ButtonTypes } from "generics/enums/button-enums";
import { Children } from "generics/types/children-types";
import useButton from "components/Button/useButton";

export interface ButtonStyles {
  capitalize: boolean;
  stretch: boolean;
  delete: boolean;
  secondary: boolean;
  error: boolean;
  round: boolean;
  small: boolean;
  mid: boolean;
}

export interface ButtonProps extends Partial<ButtonStyles> {
  href?: string;
  type?: ButtonTypes;
  children?: Children;
  disabled?: boolean;
  loading?: boolean;
  className?: string;
  onClick?: (e: MouseEvent) => void;
  onMouseOver?: (e: MouseEvent) => void;
}

function Button({
  href,
  type,
  loading,
  children,
  disabled,
  className,
  onClick,
  onMouseOver,
  ...buttonStyles
}: ButtonProps) {
  const {
    classes,
    handleClick,
    handleMouseOver
  } = useButton({ className, disabled, onClick, onMouseOver, ...buttonStyles });

  const buttonContent = (
    <>
      {loading && <FontAwesomeIcon className={buttonClasses.loading} icon={faSpinner} spin />}
      {!loading && children}
    </>
  );

  if (href) {
    return (
      <a
        className={classes}
        href={disabled ? '' : href}
      >
        {buttonContent}
      </a>
    );
  }

  return (
    <button
      type={type}
      disabled={loading || disabled}
      className={classes}
      onClick={handleClick}
      onMouseOver={handleMouseOver}
    >
      {buttonContent}
    </button>
  );
}

Button.defaultProps = {
  type: ButtonTypes.SUBMIT,
  loading: false,
  disabled: false
};

export default Button;