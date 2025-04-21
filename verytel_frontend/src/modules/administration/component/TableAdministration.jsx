import { useState, useEffect } from 'react';
import '../assets/TableAdministration.css';
import { useGetUserValidation } from '../hooks/useGetUserValidation';

export function TableAdministration() {
//   const [verification, setVerification] = useState(null);

  const { securityForm, data, list_error } = useGetUserValidation();
  const [filters, setFilters] = useState({
    verificado: false,
    noVerificado: false,
  });
 
  const handleCheckboxChange = async (type) => {
    const updatedFilters = {
      ...filters,
      [type]: !filters[type],
    };

    setFilters(updatedFilters);

    const { verificado, noVerificado } = updatedFilters;

    if (verificado && noVerificado) {
      await securityForm("todos");
    } else if (verificado) {
      await securityForm("verificado");
    } else if (noVerificado) {
      await securityForm("no-verificado");
    } else {
      return; // O podrías limpiar la tabla o mostrar un mensaje
    }
  };

  return (
    <div className="table-administration">
      <h2>Usuarios</h2>

      <div className="filters">
        <label>
          <input
            type="checkbox"
            checked={filters.verificado}
            onChange={() => handleCheckboxChange("verificado")}
          />
          Verificados
        </label>
        <label>
          <input
            type="checkbox"
            checked={filters.noVerificado}
            onChange={() => handleCheckboxChange("noVerificado")}
          />
          No verificados
        </label>
      </div>

      {list_error && <p style={{ color: 'red' }}>Error: {list_error}</p>}

<div className='table-container'>
      {data && data.length > 0 ? (
        <table className="user-table">
          <thead>
            <tr>
              <th>Nombres</th>
              <th>Apellidos</th>
              <th>Identificación</th>
              <th>Correo</th>
              <th>Celular</th>
              <th>Barrio</th>
              <th>Dirección</th>
              <th>Tipo Documento</th>
              <th>Fecha Nacimiento</th>
              <th>Sexo</th>
              <th>Antecedentes</th>
              <th>Justificación</th>
              <th>Frente de Seguridad</th>
              <th>Verificado</th>
            </tr>
          </thead>
          <tbody>
            {data.map((user, index) => (
              <tr key={index}>
                <td>{user.nombres}</td>
                <td>{user.apellidos}</td>
                <td>{user.identificacion}</td>
                <td>{user.correo}</td>
                <td>{user.celular}</td>
                <td>{user.barrio}</td>
                <td>{user.direccion}</td>
                <td>{user.tipo_documento}</td>
                <td>{user.fecha_nacimiento}</td>
                <td>{user.sexo}</td>
                <td>{user.antecedentes ? 'Sí' : 'No'}</td>
                <td>{user.justificacion_antecedentes || '—'}</td>
                <td>{user.frente_seguridad_id}</td>
                <td>{user.usuario_verificado ? '✅' : '❌'}</td>
              </tr>
            ))}
          </tbody>
        </table>
      ) : (
        <p>No hay datos para mostrar</p>
      )}

</div>
    </div>
  );
}
