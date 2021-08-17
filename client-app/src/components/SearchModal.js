import React from "react";
import { Modal } from "react-native";
import SearchModalDetail from "./SearchModalDetail";

const SearchModal = (props) => {
	return (
		<Modal
			animationType="fade"
			transparent={true}
			visible={props.visibleValue}
			onRequestClose={() => props.FsetVisible(false)}
			style={{
				opacity: 0.1,
				width: 1,
				height: 1,
			}}
		>
			<SearchModalDetail
				FsetTempText={props.FsetTempText}
				tempTextValue={props.tempTextValue}
				FsetText={props.FsetText}
				FsetVisible={props.FsetVisible}
				FsetReset={props.FsetReset}
				reset={props.reset}
			/>
		</Modal>
	);
};
export default SearchModal;
