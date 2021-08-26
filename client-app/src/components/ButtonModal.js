import React from "react";
import { Modal } from "react-native";
import ButtonModalDetail from "../components/ButtonModalDetail";

const ButtonModal = (props) => {
	return (
		<Modal
			animationType="fade"
			transparent={true}
			visible={props.visibleValue}
			onRequestClose={() => props.FsetVisible(false)}
			style={{ opacity: 0.1 }}
		>
			<ButtonModalDetail
				FsetVisible={props.FsetVisible}
				FsetCurrent={props.FsetCurrent}
				currentValue={props.currentValue}
				name={props.name}
				pressName={props.pressName}
			/>
		</Modal>
	);
};
export default ButtonModal;
