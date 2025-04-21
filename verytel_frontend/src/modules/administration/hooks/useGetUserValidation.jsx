// src/hooks/useSecurityFronts.js
import { useState, useEffect } from 'react';
import { toast } from 'react-toastify';

export const useGetUserValidation = () => {
  const [data, setData] = useState(null);
  const [list_error, setError] = useState(null);

  
    const securityForm = async (verification) => {
      try {
        const response = await fetch(`http://127.0.0.1:8000/signin/users_verification?verification=${verification}`, {
          method: "GET",
        });

        if (!response.ok) throw new Error(`HTTP error ${response.status}`);

        const result = await response.json();
        setData(result);
      } catch (err) {
        setError(err.message);
        toast.error(`Error: ${err.message}`);
      }
    };



  return {securityForm, data, list_error };
};


