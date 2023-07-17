import React, { useState } from 'react';

function App() {
  const [todos, setTodos] = useState([]);
  const [newTodo, setNewTodo] = useState('');
  const [editIndex, setEditIndex] = useState(null);
  const [editValue, setEditValue] = useState('');

  const handleInputChange = (e) => {
    if (editIndex !== null) {
      setEditValue(e.target.value);
    } else {
      setNewTodo(e.target.value);
    }
  };

  const handleFormSubmit = (e) => {
    e.preventDefault();
    if (editIndex !== null) {
      if (editValue.trim()) {
        const updatedTodos = [...todos];
        updatedTodos[editIndex] = editValue;
        setTodos(updatedTodos);
        setEditIndex(null);
        setEditValue('');
      }
    } else {
      if (newTodo.trim()) {
        setTodos([...todos, newTodo]);
        setNewTodo('');
      }
    }
  };

  const handleEditClick = (index) => {
    setEditIndex(index);
    setEditValue(todos[index]);
  };

  const handleDeleteClick = (index) => {
    const updatedTodos = todos.filter((_, i) => i !== index);
    setTodos(updatedTodos);
  };

  return (
    <div>
      <h1>Todo App</h1>
      <form onSubmit={handleFormSubmit}>
        <input
          type="text"
          value={editIndex !== null ? editValue : newTodo}
          onChange={handleInputChange}
          placeholder="Add a new todo..."
        />
        <button type="submit">{editIndex !== null ? 'Update Todo' : 'Add Todo'}</button>
      </form>
      <ul>
        {todos.map((todo, index) => (
          <li key={index}>
            {todo}
            <button onClick={() => handleEditClick(index)}>Edit</button>
            <button onClick={() => handleDeleteClick(index)}>Delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
