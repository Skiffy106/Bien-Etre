import { Text, View } from "react-native";
import {Link} from "expo-router";

export default function Index() {
  return (
    <View className="flex-1 justify-center items-center">
        <Text className="text-5xl font-bold text-background-dark">Hello Owen</Text>
        <Link href={{pathname: "/onboarding"}}>Onboarding</Link>
        <Link href={{pathname: "/home"}}>Home</Link>
        <Link href={{pathname: "/(tabs)/user/[id]", params: {id: "mason"}}}>Mason</Link>
    </View>
  );
}
