import React from "react";
import { Modal } from "react-native";
import ButtonModalDetailForSubs from "./ButtonModalDetailForSubs";

const ButtonModalForSubs = (props) => {
	return (
		<Modal
			animationType="fade"
			transparent={true}
			visible={props.visibleValue}
			onRequestClose={() => props.FsetVisible(false)}
			style={{ opacity: 0.1 }}
		>
			<ButtonModalDetailForSubs
				FsetVisible={props.FsetVisible}
				FsetCurrent={props.FsetCurrent}
				currentValue={props.currentValue}
				name={props.name}
			/>
		</Modal>
	);
};
export default ButtonModalForSubs;
