import React from "react";
import {
	View,
	Text,
	StyleSheet,
	Modal,
	ScrollView,
	Linking,
} from "react-native";
import { AntDesign } from "@expo/vector-icons";

const ArticleModal = (props) => {
	return (
		<Modal
			animationType="slide"
			transparent={false}
			visible={props.item.visible}
			onRequestClose={() =>
				props.FsetFalse(props.item.id, props.data, props.FsetData)
			}
		>
			<AntDesign.Button
				name="back"
				size={24}
				color="black"
				backgroundColor="white"
				onPress={() => {
					props.FsetFalse(props.item.id, props.data, props.FsetData);
				}}
				style={{ paddingLeft: 20 }}
			>
				<Text>뒤로 가기</Text>
			</AntDesign.Button>
			<ScrollView>
				<View style={styles.container}>
					<Text style={styles.titleSize}>{props.item.title}</Text>
					<Text />
					<Text style={styles.titleSubElement}>
						{props.item.press}
					</Text>
					<Text style={styles.titleSubElement}>
						{props.item.date}
					</Text>
					<Text style={styles.titleSubElement}>
						{props.item.reporter}
					</Text>
				</View>
				<View style={styles.container}>
					<Text style={styles.articleSize}>
						{props.item.mainText}
					</Text>
					<Text />
					{
						props.item.url.length == 1 ? <Text
							style={styles.hyperlinkSize}
							onPress={() => {
								Linking.openURL(props.item.url);
							}}
						>
							본문 보러가기 (클릭)
						</Text> : props.item.url.map((url, index) => {
							return (
								<Text
									style={styles.hyperlinkSize}
									onPress={() => {
										Linking.openURL(url);
									}}
								>
									본문 {index + 1} 보러가기 (클릭)
								</Text>
							)
						}
						)
					}
				</View>
			</ScrollView>
		</Modal>
	);
};

const styles = StyleSheet.create({
	container: {
		margin: 10,
		marginBottom: 5,
		marginTop: 5,
		backgroundColor: "white",
		borderColor: "black",
		borderWidth: 1,
		padding: 35,
		shadowColor: "#000",
		shadowOffset: {
			width: 0,
			height: 2,
		},
		shadowOpacity: 0.25,
		shadowRadius: 3.84,
		elevation: 5,
		textAlign: "left",
	},
	titleSize: {
		fontSize: 20,
	},
	titleSubElement: {
		fontSize: 13,
	},
	articleSize: {
		fontSize: 16,
	},
	hyperlinkSize: {
		fontSize: 20,
	},
});

export default ArticleModal;
