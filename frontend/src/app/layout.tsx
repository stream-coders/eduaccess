import type { Metadata } from "next";
import { inter } from "@/app/fonts";
import '@/app/globals.css';
import Footer from "@/app/components/footer";
import { AuthProvider } from "./context/AuthContext";
import Header from "@/app/components/header";
export const metadata: Metadata = {
  title: "Create Next App",
  description: "Generated by create next app",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className={inter.className}>
        <AuthProvider>
          <Header/>
          {children}
        </AuthProvider>
        <Footer />
      </body>
    </html>
  );
}
