import styles from "../styles/Home.module.css"; // Importa os estilos CSS
import { useEffect, useState } from "react";

function ContadorComMensagem() {
  // setando o estado inicial do contador
  const [contador, setContador] = useState(0);

  // Efeito colateral: exibe uma mensagem no console quando o contador muda
  useEffect(() => {
    console.log(`O contador mudou para: ${contador}`);
  }, [contador]); // Reage apenas a mudanças no contador

  const incrementar = () => {
    setContador(contador + 1);
    console.log(contador);
  }

  return (
    <main className={styles.main}>
      <p className={styles.aula}>Você clicou {contador} vezes</p>
      <button onClick={incrementar}>Incrementar</button>
    </main>
  );
}

export default ContadorComMensagem;
