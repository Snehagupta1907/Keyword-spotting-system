import "./App.css";
import { useState } from "react";
import AudioRecorder from "../src/AudioRecorder";

const App = () => {
	let [recordOption, setRecordOption] = useState("video");

	const toggleRecordOption = (type) => {
		return () => {
			setRecordOption(type);
		};
	};

	return (
		<div>
			<h1>MLSCV - Audio UI</h1>
			<div className="button-flex">
			
				<button onClick={toggleRecordOption("audio")}>Record Audio</button>
			</div>
			<div style={{marginTop:"10px"}}>
				{recordOption === "audio" ?  <AudioRecorder /> : "No Audio recorder found"}
			</div>
		</div>
	);
};

export default App;
