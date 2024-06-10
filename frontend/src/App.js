import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Navbar from "./components/Navbar";
import Home from "./components/Home";
import ImportFileS from "./components/ImportFileSale";
import ImportAllegroS from "./components/ImportAllegroSales";
import ImportWooS from "./components/ImportWooSales";
import OutputSales from "./components/OutputSales";
import OutputChart from "./components/OutputChart";
import OutputTable from "./components/OutputTable";
import WooSales from "./components/WooSales";
import WooDomainEntry from "./components/WooDomainEntry";

function App() {
  return (
    <Router>
      <Navbar />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/import-file-sale" element={<ImportFileS />} />
        <Route path="/import-allegro-sale" element={<ImportAllegroS />} />
        <Route path="/import-woo-sale" element={<ImportWooS />} />
        <Route path="/woo-domain-entry" element={<WooDomainEntry></WooDomainEntry>} />
        <Route path="/chart" element={<OutputChart />} />
        <Route path="/table" element={<OutputTable />} />
        <Route path="/output-sales" element={<OutputSales />} />
        <Route path="/woo-sales" element={<WooSales />}/>
      </Routes>
    </Router>
  );
}

export default App;
