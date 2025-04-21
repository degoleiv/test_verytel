// ProtectedRoute.jsx
import { Navigate } from "react-router-dom";
import { useValidation } from "../hooks/ValidationContext";


export function ProtectedRoute({ children }) {
  const { isPendingValidation } = useValidation();

  if (!isPendingValidation) {
    return <Navigate to="/" replace />;
  }

  return children;
}
