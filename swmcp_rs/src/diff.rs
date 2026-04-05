//! Fast string diffing implementation using the `similar` crate.

use similar::{ChangeTag, TextDiff};
use std::fmt::Write;

/// Calculate unified diff between two strings.
pub fn calculate_diff(old: &str, new: &str, context_lines: usize) -> String {
    let diff = TextDiff::from_lines(old, new);
    let mut output = String::new();
    
    for hunk in diff.unified_diff().context_radius(context_lines).iter_hunks() {
        write!(&mut output, "{}", hunk.header()).unwrap();
        
        for change in hunk.iter_changes() {
            let sign = match change.tag() {
                ChangeTag::Delete => "-",
                ChangeTag::Insert => "+",
                ChangeTag::Equal => " ",
            };
            write!(&mut output, "{}{}", sign, change.value()).unwrap();
        }
    }
    
    output
}

/// Apply unified diff to original string.
pub fn apply_diff(original: &str, diff: &str) -> anyhow::Result<String> {
    // TODO: Implement diff application logic
    // This is a placeholder - actual implementation would parse the diff
    // and apply changes line by line
    anyhow::bail!("Diff application not yet implemented")
}

#[cfg(test)]
mod tests {
    use super::*;
    
    #[test]
    fn test_calculate_diff() {
        let old = "line 1\nline 2\nline 3";
        let new = "line 1\nmodified line 2\nline 3";
        
        let diff = calculate_diff(old, new, 3);
        assert!(diff.contains("-line 2"));
        assert!(diff.contains("+modified line 2"));
    }
}
