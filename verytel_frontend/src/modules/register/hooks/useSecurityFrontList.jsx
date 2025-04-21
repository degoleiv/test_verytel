// src/hooks/useSecurityFronts.js
import { useState, useEffect } from 'react';
import {  toast } from 'react-toastify';
const useSecurityFrontsList = () => {
  const [data, setData] = useState(null);
  const [list_error, setError] = useState(null);

  useEffect(() => {
    const securityForm = async () => {
      try {
        const response = await fetch("http://127.0.0.1:8000/security/security-fronts", {
          method: "GET",
        });
        if (!response.ok) throw new Error(`HTTP error ${response.status}`);

        const result = await response.json();
        setData(result);
        
      } catch (err) {
        setError(err.message);
        toast.error("Error:", err.message);
      }
    };
    securityForm();
  }, []);

  return { data, list_error };
};

export default useSecurityFrontsList;
