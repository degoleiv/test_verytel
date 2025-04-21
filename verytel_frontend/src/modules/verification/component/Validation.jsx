import { useEffect, useState } from 'react';
import { useValidationCode } from '../hooks/useValidationCode';
import { useRefreshCode } from '../hooks/useRefreshCode';
import '../assets/Validation.css';

export function Validation() {
  const [code, setCode] = useState("");
  const { submit: submitValidation, isLoading: isLoadingValidation } = useValidationCode();
  const { submit: submitRefresh } = useRefreshCode();
  
  const [isLinkDisabled, setIsLinkDisabled] = useState(true);
  const [timer, setTimer] = useState(180); // 180 segundos = 3 minutos

  const handleSubmit = async (e) => {
    e.preventDefault();
  
    // Validación: exactamente 6 caracteres alfanuméricos
    if (!/^[a-zA-Z0-9]{6}$/.test(code)) return;
  
    await submitValidation({ code });
  };
  

  // Timer para el contador regresivo
  useEffect(() => {
    let interval;

    if (isLinkDisabled) {
      setTimer(180); // Reset del timer
      interval = setInterval(() => {
        setTimer((prev) => {
          if (prev <= 1) {
            clearInterval(interval);
            setIsLinkDisabled(false);
            return 0;
          }
          return prev - 1;
        });
      }, 1000);
    }

    return () => clearInterval(interval);
  }, [isLinkDisabled]);

  const handleResendCode = async () => {
    await submitRefresh();
    setIsLinkDisabled(true);
  };

  const formatTime = (seconds) => {
    const min = String(Math.floor(seconds / 60)).padStart(2, '0');
    const sec = String(seconds % 60).padStart(2, '0');
    return `${min}:${sec}`;
  };

  return (
    <div className="validation-container">
      <h2>Validar Código</h2>
      <p>Por favor ingresa el código de 6 dígitos enviado a su correo para validar tu usuario.</p>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          maxLength="6"
          placeholder="123456"
          value={code}
          onChange={(e) => setCode(e.target.value)}
        />
        <button type="submit" disabled={isLoadingValidation}>Validar</button>
      </form>
      <span>
        <a 
          href="#"
          onClick={(e) => {
            e.preventDefault();
            if (!isLinkDisabled) handleResendCode();
          }}
          style={{ pointerEvents: isLinkDisabled ? 'none' : 'auto', color: isLinkDisabled ? 'gray' : 'blue' }}
        >
          Clic aquí Si no llegó el código de confirmación
        </a>
        {isLinkDisabled && (
          <span style={{ marginLeft: '8px', color: 'gray' }}>
            (Reintentar en {formatTime(timer)})
          </span>
        )}
      </span>
    </div>
  );
}
