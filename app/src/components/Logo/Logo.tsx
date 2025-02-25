import styles from './Logo.module.scss';

interface LogoProps {
  className?: string;
}

function Logo({ className }: LogoProps) {
  return (
    <div className={`${styles.logo} ${className}`}>
      Quote Master
    </div>
  );
}

export default Logo;