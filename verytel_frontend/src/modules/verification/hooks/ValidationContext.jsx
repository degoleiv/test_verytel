// ValidationContext.jsx
import { createContext, useContext, useState } from 'react';

const ValidationContext = createContext();

export const ValidationProvider = ({ children }) => {
  const [isPendingValidation, setIsPendingValidation] = useState(false);

  return (
    <ValidationContext.Provider value={{ isPendingValidation, setIsPendingValidation }}>
      {children}
    </ValidationContext.Provider>
  );
};

export const useValidation = () => useContext(ValidationContext);
