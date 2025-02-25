import { MouseEvent, useMemo } from "react";
import { ButtonProps } from "./Button";

import buttonClasses from './Button.module.scss';

function useButton({ className, disabled, onClick, onMouseOver, ...buttonStyles }: ButtonProps) {
  const classesToApply: string = useMemo(() => {
    return Object.keys(buttonStyles)
      .map((cls: string): string => ((buttonStyles as any)[cls] ? buttonClasses[cls] : ''))
      .concat(buttonClasses.button, className ?? '')
      .join(' ');
  }, [className, buttonStyles]);

  const handleClick = (e: MouseEvent): void => {
    if (disabled) return;
    onClick && onClick(e);
  };

  const handleMouseOver = (e: MouseEvent): void => {
    if (disabled) return;
    onMouseOver && onMouseOver(e);
  };

  return {
    classes: classesToApply,
    handleClick,
    handleMouseOver,
  };
}

export default useButton;