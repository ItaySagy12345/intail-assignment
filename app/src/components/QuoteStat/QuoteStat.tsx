import styles from './QuoteStat.module.scss';

interface QuoteStatProps {
  stat: string;
  value?: string;
}

function QuoteStat({ stat, value }: QuoteStatProps) {
  const FALLBACK = 'N/A';

  return (
    <div className={styles.quoteStat}>
      <p className={styles.stat}>{stat ?? FALLBACK}</p>
      <p className={styles.value}>{value ?? FALLBACK}</p>
    </div>
  );
}

export default QuoteStat;