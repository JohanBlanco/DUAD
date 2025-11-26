# Tabla Informativa sobre SELECT, ORDER BY, LIMIT, GROUP BY y JOINs

  -----------------------------------------------------------------------------------------------------------------------
  Concepto        Descripción           Uso común          Ejemplo
  --------------- --------------------- ------------------ --------------------------------------------------------------
  **SELECT**      Permite elegir qué    Obtener datos      `SELECT name, age FROM users;`
                  columnas consultar de específicos o      
                  una tabla.            todos los datos    
                                        (\*).              

  **ORDER BY**    Ordena los resultados Ordenar por        `SELECT * FROM products ORDER BY price DESC;`
                  en ascendente (ASC) o fechas, precios,   
                  descendente (DESC).   nombres, etc.      

  **LIMIT**       Restringe la cantidad Obtener top n      `SELECT * FROM logs LIMIT 10;`
                  de filas devueltas.   registros,         
                                        paginación.        

  **GROUP BY**    Agrupa filas para     Reportes y         `SELECT category, COUNT(*) FROM products GROUP BY category;`
                  funciones agregadas   estadísticas.      
                  (COUNT, SUM, AVG...).                    

  **INNER JOIN**  Solo registros        Relaciones         `SELECT * FROM A INNER JOIN B ON A.id = B.a_id;`
                  coincidentes entre    directas           
                  tablas.               uno-a-muchos.      

  **LEFT JOIN**   Todos los registros   Encontrar          `SELECT * FROM A LEFT JOIN B ON A.id = B.a_id;`
                  de la izquierda +     elementos sin      
                  coincidencias de la   relación.          
                  derecha.                                 

  **RIGHT JOIN**  Todos los registros   Reportes centrados `SELECT * FROM A RIGHT JOIN B ON A.id = B.a_id;`
                  de la derecha +       en la tabla        
                  coincidencias de la   derecha.           
                  izquierda (no en                         
                  SQLite).                                 

  **FULL OUTER    Todos los registros   Combinar conjuntos `SELECT * FROM A FULL JOIN B ON A.id = B.a_id;`
  JOIN**          aunque no haya        completos.         
                  coincidencia.                            
  -----------------------------------------------------------------------------------------------------------------------
