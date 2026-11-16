import { BrowserRouter, Routes, Route } from "react-router-dom";
import LoginPage from "./features/auth/LoginPage";
import HomePage from "./features/notes/HomePage";
import NotesPage from "./features/notes/NotesPage";

function App() {
  return (
    <>
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<LoginPage />}></Route>
          <Route path="/home" element={<HomePage />}>
            <Route path="notes" element={<NotesPage />} />
          </Route>
        </Routes>
      </BrowserRouter>
    </>
  );
}

export default App;
