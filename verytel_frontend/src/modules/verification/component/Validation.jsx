import { useState } from 'react';
import { useValidationCode } from '../hooks/useValidationCode';  // Asegúrate de importar el hook correctamente
import '../assets/Validation.css';

export function Validation() {
  const [code, setCode] = useState("");
  const { submit, isLoading, response, error } = useValidationCode(); // 

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    if (!/^\d{6}$/.test(code)) {
      
      return; // Validación de formato de código
    }

     await submit({ code, id: 123 }); 

  };

  return (
    <div className="validation-container">
      <h2>Validar Código</h2>
      <p>Por favor ingresa el código de 6 dígitos para validar tu usuario.</p>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          maxLength="6"
          placeholder="123456"
          value={code}
          onChange={(e) => setCode(e.target.value)}
        />
        <button type="submit" disabled={isLoading}>Validar</button>
      </form>

    </div>
  );
}
