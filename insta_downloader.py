import os
import sys
import re
import subprocess

def extract_shortcode(url):
    """인스타 URL에서 shortcode 추출"""
    pattern = r'instagram\.com/p/([^/?]+)'
    match = re.search(pattern, url)
    if match:
        return match.group(1)
    else:
        return None

def download_instagram_video(url, output_dir=None):
    """인스타 URL에서 동영상만 다운로드"""
    shortcode = extract_shortcode(url)
    
    if not shortcode:
        print(f"오류: 올바른 인스타그램 URL이 아닙니다: {url}")
        return None
    
    # 출력 디렉토리 설정
    if not output_dir:
        output_dir = os.getcwd()
    
    # 다운로드 진행
    print(f"'{shortcode}' 게시물의 동영상을 다운로드합니다...")
    
    try:
        # instaloader 명령어 실행
        cmd = ["instaloader", "--no-pictures", "--no-metadata-json", "--", f"-{shortcode}"]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        
        # 다운로드된 파일 경로 찾기
        download_dir = os.path.join(os.getcwd(), f"-{shortcode}")
        video_files = [f for f in os.listdir(download_dir) if f.endswith('.mp4')]
        
        if not video_files:
            print("동영상 파일을 찾을 수 없습니다. 게시물에 동영상이 없을 수 있습니다.")
            return None
        
        # 다운로드된 파일 경로 반환
        video_paths = [os.path.join(download_dir, video) for video in video_files]
        return video_paths
        
    except subprocess.CalledProcessError as e:
        print(f"다운로드 오류: {e}")
        print(f"오류 메시지: {e.stderr}")
        return None
    except Exception as e:
        print(f"예상치 못한 오류: {e}")
        return None

if __name__ == "__main__":
    # 명령줄 인자로 URL 받기
    if len(sys.argv) < 2:
        print("사용법: python insta_downloader.py <인스타그램_URL>")
        sys.exit(1)
    
    url = sys.argv[1]
    video_paths = download_instagram_video(url)
    
    if video_paths:
        print("\n다운로드 완료!")
        print("다운로드된 동영상 파일:")
        for path in video_paths:
            print(f"- {path}")
    else:
        print("동영상 다운로드에 실패했습니다.") 